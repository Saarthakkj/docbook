'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import URLInput from '../../components/URLInput';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../components/ui/card';
import { CheckCircleIcon, BookOpenIcon } from 'lucide-react';

export default function UploadPage() {
  const router = useRouter();
  const [isProcessing, setIsProcessing] = useState(false);
  const [status, setStatus] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (url) => {
    setIsProcessing(true);
    setStatus('Processing documentation URL...');
    setSuccess(false);

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Failed to process the URL');
      }

      setStatus('Documentation processed successfully! Redirecting to chat...');
      setSuccess(true);
      
      // Short delay before redirecting to chat page
      // Add a query parameter to indicate a successful upload just happened
      setTimeout(() => {
        router.push('/chat?from=upload&success=true');
      }, 1500);
      
    } catch (error) {
      console.error('Error processing URL:', error);
      setStatus(`Error: ${error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] px-4">
      <div className="w-full max-w-md mb-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold flex items-center justify-center gap-2 mb-2">
            <BookOpenIcon className="h-8 w-8 text-blue-600" />
            Documentation Chat
          </h1>
          <p className="text-lg text-muted-foreground max-w-lg">
            Enter the URL of any documentation page and ask questions about it using AI.
          </p>
        </div>

        <URLInput onSubmit={handleSubmit} />
        
        {status && (
          <div className="mt-6 animate-fade-in">
            <Card className={`border ${success ? 'border-green-200 bg-green-50' : 'border-blue-200 bg-blue-50'}`}>
              <CardContent className="pt-6">
                <div className="flex items-start gap-3">
                  {success ? (
                    <CheckCircleIcon className="h-5 w-5 text-green-600 mt-0.5" />
                  ) : (
                    <div className="flex-shrink-0 h-5 w-5 mt-0.5">
                      <div className="animate-spin h-5 w-5 border-2 border-blue-600 border-t-transparent rounded-full" />
                    </div>
                  )}
                  <div>
                    <p className={`text-sm ${success ? 'text-green-700' : 'text-blue-700'}`}>
                      {status}
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        )}
      </div>
    </div>
  );
}