import { NextApiRequest, NextApiResponse } from 'next';
import { queryRAG, getRAGStatus } from '../../lib/rag';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const { query } = req.body;

    if (!query) {
      return res.status(400).json({ message: 'Query is required' });
    }

    // Check if RAG system is initialized
    const ragStatus = getRAGStatus();
    if (!ragStatus.initialized) {
      return res.status(400).json({ 
        message: 'No documentation loaded',
        error: 'Please upload documentation before chatting. You can do this from the upload page.' 
      });
    }

    // Query the RAG system
    const result = await queryRAG(query);

    // Return the response
    return res.status(200).json({
      response: result.response,
      usedChunks: result.usedChunks
    });

  } catch (error) {
    console.error('Error processing chat query:', error);
    return res.status(500).json({ 
      message: 'Failed to process your query',
      error: error.message || 'Unknown error'
    });
  }
}