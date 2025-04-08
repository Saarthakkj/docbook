'use client';
import React from 'react';
import { cn } from '@/lib/utils';
import { Card } from './ui/card';
import { UserIcon, BotIcon } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import rehypeHighlight from 'rehype-highlight';
import rehypeRaw from 'rehype-raw';

type MessageProps = {
  content: string;
  isUser: boolean;
  timestamp?: Date;
};

export default function Message({ content, isUser, timestamp = new Date() }: MessageProps) {
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className="flex items-start gap-3 max-w-[80%]">
        {!isUser && (
          <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0 mt-1">
            <BotIcon className="h-4 w-4 text-blue-600" />
          </div>
        )}
        
        <Card
          className={cn(
            "px-4 py-3 text-sm",
            isUser 
              ? "bg-blue-600 text-white border-blue-600" 
              : "bg-gray-50 text-gray-800 border-gray-100"
          )}
        >
          {isUser ? (
            <div className="whitespace-pre-wrap">{content}</div>
          ) : (
            <div className="markdown-content">
              <ReactMarkdown 
                rehypePlugins={[rehypeHighlight, rehypeRaw]}
                components={{
                  code({node, inline, className, children, ...props}) {
                    const match = /language-(\w+)/.exec(className || '');
                    return !inline && match ? (
                      <pre className="rounded bg-slate-800 p-2 my-2 overflow-x-auto">
                        <code className={className} {...props}>
                          {children}
                        </code>
                      </pre>
                    ) : (
                      <code className="font-mono bg-slate-200 px-1 py-0.5 rounded text-slate-800" {...props}>
                        {children}
                      </code>
                    );
                  }
                }}
              >
                {content}
              </ReactMarkdown>
            </div>
          )}
          <div
            className={cn(
              "text-xs mt-1",
              isUser ? "text-blue-200" : "text-gray-500"
            )}
          >
            {timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </div>
        </Card>
        
        {isUser && (
          <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center flex-shrink-0 mt-1">
            <UserIcon className="h-4 w-4 text-white" />
          </div>
        )}
      </div>
    </div>
  );
}