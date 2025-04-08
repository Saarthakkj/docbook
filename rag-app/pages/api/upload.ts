import { NextApiRequest, NextApiResponse } from 'next';
import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import { chunkMarkdown } from '../../lib/chunkMarkdown';
import { initializeRAG } from '../../lib/rag';

// Ensure data directory exists
const dataDir = path.join(process.cwd(), 'data');
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

// Maximum number of chunks to process
const MAX_CHUNKS = 750;

const contextPath = path.join(dataDir, 'context.md');

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const { url } = req.body;

    if (!url) {
      return res.status(400).json({ message: 'URL is required' });
    }

    // Clear previous markdown file if it exists
    if (fs.existsSync(contextPath)) {
      fs.writeFileSync(contextPath, '');
    }

    // Run the Python script with the URL as an argument
    // Updated path to point within the project's scripts directory
    const pythonScriptPath = path.join(process.cwd(), 'scripts', 'scrape_to_md.py');
    
    console.log(`Starting Python script: ${pythonScriptPath}`);
    console.log(`Processing URL: ${url}`);
    
    // Execute the Python script as a child process
    const pythonProcess = spawn('python', [pythonScriptPath, url, contextPath]);
    
    let scriptOutput = '';
    let scriptError = '';

    pythonProcess.stdout.on('data', (data) => {
      scriptOutput += data.toString();
      console.log(`Python script output: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      scriptError += data.toString();
      console.error(`Python script error: ${data}`);
    });

    // Wait for the Python script to complete
    const exitCode = await new Promise((resolve) => {
      pythonProcess.on('close', resolve);
    });

    if (exitCode !== 0) {
      console.error(`Python script exited with code ${exitCode}`);
      console.error(`Error output: ${scriptError}`);
      return res.status(500).json({ 
        message: 'Failed to process the URL',
        error: scriptError || 'Unknown error'
      });
    }

    // Read the generated markdown file
    if (!fs.existsSync(contextPath)) {
      return res.status(500).json({ 
        message: 'Failed to generate markdown content',
        error: 'Markdown file not found'
      });
    }

    const markdownContent = fs.readFileSync(contextPath, 'utf-8');
    
    if (!markdownContent || markdownContent.trim().length === 0) {
      return res.status(500).json({ 
        message: 'Failed to generate markdown content',
        error: 'Generated markdown is empty'
      });
    }

    console.log(`Successfully generated markdown (${markdownContent.length} characters)`);

    // Chunk the markdown content
    let chunks = chunkMarkdown(markdownContent);
    console.log(`Split markdown into ${chunks.length} chunks`);
    
    // Limit the number of chunks to process
    if (chunks.length > MAX_CHUNKS) {
      console.log(`Limiting chunks from ${chunks.length} to ${MAX_CHUNKS}`);
      chunks = chunks.slice(0, MAX_CHUNKS);
    }

    // Initialize the RAG system with the chunks
    await initializeRAG(chunks);

    // Return success response
    return res.status(200).json({ 
      message: 'URL processed successfully',
      chunkCount: chunks.length,
      limitApplied: chunks.length === MAX_CHUNKS
    });

  } catch (error) {
    console.error('Error processing URL:', error);
    return res.status(500).json({ 
      message: 'Failed to process the URL',
      error: error.message || 'Unknown error'
    });
  }
}