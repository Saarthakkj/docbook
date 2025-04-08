'use client';
import React, { useState, useRef, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Message from './Message';
import { Input } from './ui/input';
import { Button } from './ui/button';
import { Card, CardContent, CardHeader, CardTitle, CardFooter, CardDescription } from './ui/card';
import { SendIcon, AlertCircleIcon, MessageCircleIcon, UploadIcon, BotIcon } from 'lucide-react';

type ChatMessage = {
  content: string;
  isUser: boolean;
  timestamp: Date;
};

export default function ChatBox() {
  const router = useRouter();
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      content: 'I can answer questions about the documentation you provided. What would you like to know?',
      isUser: false,
      timestamp: new Date(),
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [noDocsError, setNoDocsError] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Focus input on initial load
  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!query.trim()) return;
    
    const userMessage: ChatMessage = {
      content: query,
      isUser: true,
      timestamp: new Date(),
    };
    
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setError('');
    setNoDocsError(false);
    
    // Store the query and clear the input
    const currentQuery = query;
    setQuery('');
    
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: currentQuery }),
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        // Check if this is a "no documentation" error
        if (data.message === 'No documentation loaded') {
          setNoDocsError(true);
          throw new Error(data.error || 'Please upload documentation before chatting');
        }
        throw new Error(data.message || 'Failed to get a response');
      }
      
      const botMessage: ChatMessage = {
        content: data.response,
        isUser: false,
        timestamp: new Date(),
      };
      
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error('Error querying chat API:', err);
      setError(err.message || 'Failed to get a response');
      
      // Add error message to chat
      if (err.message) {
        const errorMessage: ChatMessage = {
          content: `Error: ${err.message}`,
          isUser: false,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMessage]);
      }
    } finally {
      setIsLoading(false);
      // Focus input after sending
      setTimeout(() => {
        inputRef.current?.focus();
      }, 100);
    }
  };

  const goToUpload = () => {
    router.push('/upload');
  };

  return (
    <Card className="flex flex-col h-[80vh] w-full max-w-4xl mx-auto border rounded-lg overflow-hidden shadow-md">
      <CardHeader className="bg-blue-600 text-white py-4 px-6 shadow-sm">
        <div className="flex items-center justify-between">
          <CardTitle className="text-xl font-semibold flex items-center gap-2">
            <MessageCircleIcon className="h-5 w-5" />
            Documentation Chat
          </CardTitle>
          <Button 
            variant="outline" 
            size="sm" 
            className="bg-white/10 text-white border-white/20 hover:bg-white/20"
            onClick={goToUpload}
          >
            <UploadIcon className="h-4 w-4 mr-2" />
            New Doc
          </Button>
        </div>
      </CardHeader>
      
      <CardContent className="flex-1 p-4 overflow-y-auto bg-slate-50">
        <div className="space-y-4">
          {messages.map((message, index) => (
            <Message
              key={index}
              content={message.content}
              isUser={message.isUser}
              timestamp={message.timestamp}
            />
          ))}
          
          {isLoading && (
            <div className="flex justify-start mb-4">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0">
                  <BotIcon className="h-4 w-4 text-blue-600" />
                </div>
                
                <Card className="bg-gray-50 text-gray-800 border-gray-100 px-4 py-3">
                  <div className="flex space-x-2">
                    <div className="w-2 h-2 rounded-full bg-gray-500 animate-bounce"></div>
                    <div className="w-2 h-2 rounded-full bg-gray-500 animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                    <div className="w-2 h-2 rounded-full bg-gray-500 animate-bounce" style={{ animationDelay: '0.4s' }}></div>
                  </div>
                </Card>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>
      </CardContent>
      
      <CardFooter className="p-4 bg-white border-t">
        <form onSubmit={handleSubmit} className="w-full space-y-2">
          {error && (
            <div className="mb-2">
              <div className="flex items-center gap-2 text-red-500 text-sm">
                <AlertCircleIcon className="h-4 w-4" />
                <p>{error}</p>
                {noDocsError && (
                  <Button
                    type="button"
                    size="sm"
                    variant="outline"
                    className="ml-2 text-xs border-red-200 text-red-600 hover:bg-red-50"
                    onClick={goToUpload}
                  >
                    Upload Documentation
                  </Button>
                )}
              </div>
            </div>
          )}
          
          <div className="flex space-x-2">
            <Input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask a question about the documentation..."
              className="flex-1"
              disabled={isLoading}
            />
            <Button
              type="submit"
              disabled={isLoading || !query.trim()}
              className="bg-blue-600 hover:bg-blue-700"
            >
              <SendIcon className="h-4 w-4" />
              <span className="sr-only">Send</span>
            </Button>
          </div>
        </form>
      </CardFooter>
    </Card>
  );
}