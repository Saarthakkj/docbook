'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import URLInput from '../../components/URLInput';
import { useToast } from "@/components/ui/use-toast";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function UploadPage() {
  const router = useRouter();
  const { toast } = useToast();
  const [isProcessing, setIsProcessing] = useState(false);

  const handleSubmit = async (url: string) => {
    setIsProcessing(true);
    toast({
      title: "Processing URL...",
      description: "Fetching and embedding documentation. This may take a moment.",
    });

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.message || 'Failed to process the URL');
      }

      toast({
        title: "Success!",
        description: `Documentation processed (${result.chunkCount} chunks). Redirecting to chat...`,
        variant: "default", // Use default variant for success
      });
      
      // Short delay before redirecting to chat page
      setTimeout(() => {
        router.push('/chat?from=upload&success=true');
      }, 1500);
      
    } catch (error: any) {
      console.error('Error processing URL:', error);
      toast({
        title: "Upload Failed",
        description: error.message || "An unknown error occurred.",
        variant: "destructive",
      });
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex justify-center items-start pt-10 min-h-[70vh]">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle className="text-2xl">Upload Documentation</CardTitle>
          <CardDescription>
            Enter the URL of the documentation you want to chat with. The content will be fetched, processed, and embedded for Q&A.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <URLInput onSubmit={handleSubmit} />
        </CardContent>
      </Card>
    </div>
  );
}