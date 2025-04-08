import { NextApiRequest, NextApiResponse } from 'next';
import { getRAGStatus } from '../../lib/rag';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'GET') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    // Get the current status of the RAG system
    const status = getRAGStatus();
    
    return res.status(200).json(status);
  } catch (error) {
    console.error('Error getting RAG status:', error);
    return res.status(500).json({ 
      message: 'Failed to get RAG status',
      error: error.message || 'Unknown error'
    });
  }
}