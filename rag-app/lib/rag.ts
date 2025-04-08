import { GoogleGenerativeAI } from '@google/generative-ai';
import { getEmbedding, computeCosineSimilarity } from './embed';
import fs from 'fs';
import path from 'path';

// Initialize the Google Generative AI with your API key
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || '');

// Path to store embedded chunks
const embeddingsFilePath = path.join(process.cwd(), 'data', 'embeddings.json');

// Create a global in-memory store for our embedded chunks
// Format: { id: string, text: string, embedding: number[] }[]
let embeddedChunks: { id: string; text: string; embedding: number[] }[] = [];

// Load embeddings from file if they exist
try {
  if (fs.existsSync(embeddingsFilePath)) {
    const data = fs.readFileSync(embeddingsFilePath, 'utf-8');
    embeddedChunks = JSON.parse(data);
    console.log(`Loaded ${embeddedChunks.length} embedded chunks from disk`);
  }
} catch (error) {
  console.error('Error loading embeddings from disk:', error);
  embeddedChunks = [];
}

/**
 * Save the current embeddings to disk
 */
function saveEmbeddingsToDisk() {
  try {
    const dataDir = path.join(process.cwd(), 'data');
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    
    fs.writeFileSync(embeddingsFilePath, JSON.stringify(embeddedChunks), 'utf-8');
    console.log(`Saved ${embeddedChunks.length} embedded chunks to disk`);
  } catch (error) {
    console.error('Error saving embeddings to disk:', error);
  }
}

export async function initializeRAG(chunks: string[]) {
  try {
    console.log(`Initializing RAG with ${chunks.length} chunks`);
    embeddedChunks = [];
    
    // Process chunks in batches to avoid rate limiting issues
    const batchSize = 10;
    for (let i = 0; i < chunks.length; i += batchSize) {
      const batch = chunks.slice(i, i + batchSize);
      
      // Process batch in parallel
      const batchPromises = batch.map(async (chunk, index) => {
        const embedding = await getEmbedding(chunk);
        return {
          id: `chunk-${i + index}`,
          text: chunk,
          embedding
        };
      });
      
      const batchResults = await Promise.all(batchPromises);
      embeddedChunks.push(...batchResults);
      
      // Simple progress logging
      console.log(`Embedded ${Math.min(i + batchSize, chunks.length)}/${chunks.length} chunks`);
      
      // Add a small delay between batches to avoid rate limiting
      if (i + batchSize < chunks.length) {
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    // Save embeddings to disk after initialization
    saveEmbeddingsToDisk();
    
    console.log('RAG initialization complete');
    return true;
  } catch (error) {
    console.error('Error initializing RAG:', error);
    throw new Error('Failed to initialize RAG');
  }
}

export async function queryRAG(question: string, topK: number = 3) {
  try {
    if (embeddedChunks.length === 0) {
      throw new Error('RAG system not initialized with content');
    }
    
    // Get embedding for the question
    const questionEmbedding = await getEmbedding(question);
    
    // Calculate similarity scores for all chunks
    const scoredChunks = embeddedChunks.map(chunk => ({
      ...chunk,
      score: computeCosineSimilarity(questionEmbedding, chunk.embedding)
    }));
    
    // Sort by similarity score (descending) and take top K
    const topChunks = scoredChunks
      .sort((a, b) => b.score - a.score)
      .slice(0, topK);
    
    // Extract just the text from the top chunks
    const relevantContext = topChunks.map(chunk => chunk.text).join("\n\n");
    
    // Get the Gemini model for generating responses
    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash-lite-preview-02-05" });
    
    // Create the prompt with context and question
    const prompt = `You are a helpful assistant. Use the following documentation context to answer the question.

Context:
${relevantContext}

Question:
${question}

If the answer cannot be found in the context, say "I don't have enough information to answer that question based on the provided documentation."`;
    
    // Generate a response
    const result = await model.generateContent(prompt);
    const response = result.response.text();
    
    return { 
      response,
      usedChunks: topChunks.map(chunk => ({ id: chunk.id, text: chunk.text }))
    };
  } catch (error) {
    console.error('Error querying RAG:', error);
    throw new Error('Failed to query RAG');
  }
}

export function getRAGStatus() {
  // Add logging to help debug the initialization state
  console.log(`RAG status check: ${embeddedChunks.length} chunks loaded, initialized: ${embeddedChunks.length > 0}`);
  
  return {
    initialized: embeddedChunks.length > 0,
    chunkCount: embeddedChunks.length
  };
}