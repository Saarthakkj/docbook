import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] text-center">
      <h1 className="text-4xl font-bold tracking-tight mb-4">Documentation RAG App</h1>
      <p className="text-lg text-muted-foreground mb-8 max-w-xl">
        Upload a documentation URL, and chat with its content using the power of Gemini.
        Get answers, summaries, and insights instantly.
      </p>
      <Button asChild size="lg">
        <Link href="/upload">Get Started</Link>
      </Button>
    </div>
  );
}