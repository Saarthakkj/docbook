'use client';
import { useState } from 'react';
import { Input } from './ui/input';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from './ui/card';
import { LinkIcon, ArrowRightIcon, AlertCircleIcon, CheckCircleIcon } from 'lucide-react';

export default function URLInput({ onSubmit }) {
  const [url, setUrl] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Basic URL validation
    if (!url.trim()) {
      setError('Please enter a URL');
      return;
    }
    
    try {
      // Check if it's a valid URL
      new URL(url);
      setError('');
      
      setIsSubmitting(true);
      
      try {
        await onSubmit(url);
      } catch (err) {
        console.error('Error submitting URL:', err);
        setError(err.message || 'Failed to process URL');
        setIsSubmitting(false);
      }
    } catch (err) {
      setError('Please enter a valid URL');
    }
  };

  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <LinkIcon className="h-5 w-5" />
          Enter Documentation URL
        </CardTitle>
        <CardDescription>
          Provide a URL to documentation you want to explore through chat
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit}>
          <div className="flex flex-col space-y-4">
            <div className="space-y-2">
              <Input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://docs.example.com"
                className="w-full"
                disabled={isSubmitting}
              />
              
              {error && (
                <div className="flex items-center gap-2 text-red-500 text-sm mt-1">
                  <AlertCircleIcon className="h-4 w-4" />
                  <span>{error}</span>
                </div>
              )}
            </div>
            
            <Button 
              type="submit" 
              className="w-full"
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <>
                  <span className="mr-2">Processing</span>
                  <div className="animate-spin h-4 w-4 border-2 border-current border-t-transparent rounded-full" />
                </>
              ) : (
                <>
                  <span className="mr-2">Process URL</span>
                  <ArrowRightIcon className="h-4 w-4" />
                </>
              )}
            </Button>
          </div>
        </form>
      </CardContent>
      <CardFooter className="text-xs text-muted-foreground">
        <p>The URL will be processed and content will be available for chat</p>
      </CardFooter>
    </Card>
  );
}