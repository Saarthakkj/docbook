'use client';
import { useEffect, useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import ChatBox from '../../components/ChatBox';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '../../components/ui/card';
import { Button } from '../../components/ui/button';
import { BookOpenIcon, RefreshCwIcon, UploadIcon, AlertTriangleIcon } from 'lucide-react';

export default function ChatPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const fromUpload = searchParams.get('from') === 'upload';
  const uploadSuccess = searchParams.get('success') === 'true';
  
  // Always initialize with "true" if coming from a successful upload, otherwise we'll check
  const [isInitialized, setIsInitialized] = useState(fromUpload && uploadSuccess);
  const [isChecking, setIsChecking] = useState(!fromUpload || !uploadSuccess);
  const [error, setError] = useState(null);
  
  // Add a retry mechanism
  const [retryCount, setRetryCount] = useState(0);
  const maxRetries = 3;

  useEffect(() => {
    // If coming from a successful upload, assume it's initialized but verify in background
    if (fromUpload && uploadSuccess) {
      console.log('Coming from successful upload, setting initialized to true');
      setIsInitialized(true);
      
      // Verify in the background without blocking UI
      verifyRagStatus(false);
      return;
    }
    
    // Otherwise check if RAG is initialized when the component mounts
    verifyRagStatus(true);
    
  }, [router, fromUpload, uploadSuccess]);
  
  // Function to verify RAG status with retry logic
  const verifyRagStatus = async (blockUI = true) => {
    if (blockUI) {
      setIsChecking(true);
    }
    
    try {
      console.log('Checking RAG status...');
      const response = await fetch('/api/status', {
        method: 'GET',
        // Add cache busting parameter to avoid cached responses
        headers: {
          'Cache-Control': 'no-cache',
          'Pragma': 'no-cache'
        }
      });
      
      if (response.ok) {
        const data = await response.json();
        console.log('RAG status response:', data);
        
        // Update state based on response
        setIsInitialized(data.initialized);
        
        // If we're redirected from upload but system reports not initialized,
        // and we haven't exceeded max retries, try again after a delay
        if (fromUpload && uploadSuccess && !data.initialized && retryCount < maxRetries) {
          console.log(`RAG not initialized yet, retrying (${retryCount + 1}/${maxRetries})...`);
          setRetryCount(prev => prev + 1);
          
          // Wait 2 seconds and try again
          setTimeout(() => verifyRagStatus(false), 2000);
          return;
        }
        
        // Only redirect if explicitly not initialized and not from upload page
        if (!data.initialized && !fromUpload) {
          console.log('RAG not initialized and not from upload, redirecting to upload');
          router.push('/upload');
        }
      } else {
        // Handle errors but don't redirect if from upload
        console.error('Failed to check RAG status:', response.status);
        if (!fromUpload) {
          setError('Failed to check document status');
        }
      }
    } catch (error) {
      console.error('Error checking RAG status:', error);
      if (!fromUpload) {
        setError('Network error when checking document status');
      }
    } finally {
      if (blockUI) {
        setIsChecking(false);
      }
    }
  };

  // If just checking in background, skip loading UI
  if (isChecking && (!fromUpload || !uploadSuccess)) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[70vh]">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-700 mb-4 mx-auto"></div>
          <p className="text-lg font-medium">Checking document status...</p>
          <p className="text-sm text-muted-foreground mt-2">This will just take a moment</p>
        </div>
      </div>
    );
  }

  if (error && !isInitialized) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[70vh] px-4">
        <Card className="max-w-md w-full text-center border-red-200">
          <CardHeader>
            <div className="mx-auto bg-red-100 rounded-full w-16 h-16 flex items-center justify-center mb-2">
              <AlertTriangleIcon className="h-8 w-8 text-red-600" />
            </div>
            <CardTitle className="text-xl">Error</CardTitle>
            <CardDescription className="text-red-600 font-medium">{error}</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="mb-6 text-muted-foreground">You can try loading documentation again</p>
            <Button
              onClick={() => router.push('/upload')}
              className="mx-auto"
            >
              <UploadIcon className="h-4 w-4 mr-2" />
              Upload Documentation
            </Button>
            <Button
              variant="outline"
              onClick={() => verifyRagStatus(true)}
              className="mt-2 mx-auto"
            >
              <RefreshCwIcon className="h-4 w-4 mr-2" />
              Retry
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  // Only show this if not from upload page and not initialized
  if (!isInitialized && !fromUpload) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[70vh] px-4">
        <Card className="max-w-md w-full text-center">
          <CardHeader>
            <div className="mx-auto bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mb-2">
              <BookOpenIcon className="h-8 w-8 text-blue-600" />
            </div>
            <CardTitle className="text-xl">No Documentation Loaded</CardTitle>
            <CardDescription>Please upload documentation before starting a chat.</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="mb-6 text-muted-foreground">Upload a documentation URL to get started</p>
            <Button
              onClick={() => router.push('/upload')}
              className="mx-auto"
            >
              <UploadIcon className="h-4 w-4 mr-2" />
              Upload Documentation
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="container mx-auto py-6 px-4">
      <ChatBox />
    </div>
  );
}