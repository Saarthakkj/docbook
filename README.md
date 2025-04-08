# LLMDocs-R: RAG-Powered Documentation Assistant

A Next.js application that implements Retrieval-Augmented Generation (RAG) to provide intelligent Q&A on documentation content. The system scrapes documentation websites, processes the content, and leverages embeddings with Google's Gemini model to deliver accurate answers.

## Overview

LLMDocs-R combines web scraping, vector embeddings, and large language models to create a powerful documentation assistant. It follows these key steps:

1. **Documentation Scraping**: Crawls documentation websites to extract content
2. **Content Processing**: Chunks text into manageable pieces and creates embeddings
3. **RAG Implementation**: Uses similarity search to find relevant context for user queries
4. **Response Generation**: Leverages Google's Gemini model to generate accurate, contextual answers

## Features

- **Website Documentation Scraping**: Crawl any documentation website to extract content
- **Smart Content Chunking**: Divide documentation into semantically meaningful chunks
- **Vector Embeddings**: Create and store embeddings for efficient similarity search
- **Interactive Chat Interface**: Ask questions and get answers through a clean, user-friendly UI
- **URL-based Content Upload**: Add new documentation by simply providing a URL
- **Markdown Rendering**: Code blocks and formatting are properly displayed in responses

## Technology Stack

- **Frontend**: Next.js with React and Tailwind CSS
- **Backend**: Next.js API routes
- **RAG Engine**: Custom implementation using vector embeddings
- **Models**: Google's Gemini API for generating responses
- **Scraping**: crawl4ai library for documentation extraction
- **Storage**: File-based storage for embeddings and raw content

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+ (for the scraping functionality)
- Google Gemini API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/llmdocs-r.git
cd llmdocs-r/rag-app
```

2. Install dependencies
```bash
npm install
pip install -r requirements.txt  # For Python dependencies
```

3. Create a `.env.local` file in the rag-app directory with your API key:
```
GEMINI_API_KEY=your_api_key_here
```

4. Start the development server
```bash
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## Usage

### Adding Documentation

1. Navigate to the "Upload" page
2. Enter the URL of the documentation site you want to process
3. Click "Crawl" and wait for the process to complete
4. The system will automatically index the content for future queries

### Asking Questions

1. Navigate to the "Chat" page
2. Type your question in the input field
3. Receive answers based on the documentation content
4. View code snippets with proper syntax highlighting

## How It Works

### RAG Architecture

The application uses a three-step process for answering questions:

1. **Retrieval**: When a question is asked, the system finds the most relevant chunks from the documentation based on embedding similarity.
2. **Augmentation**: The retrieved context is combined with the user's question to create a comprehensive prompt.
3. **Generation**: Google's Gemini model uses the augmented prompt to generate an accurate, specific answer.

### Embedding Process

1. Documentation is chunked into smaller pieces
2. Each chunk is converted into a vector embedding
3. Embeddings are stored for efficient similarity search
4. User questions are also converted to embeddings for comparison

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This tool relies on the [crawl4ai](https://docs.crawl4ai.com) library for web crawling functionality
- Powered by Google's Gemini API for natural language generation
- Built with Next.js and Tailwind CSS
