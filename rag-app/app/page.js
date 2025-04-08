export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh]">
      <h1 className="text-3xl font-bold mb-6">Documentation RAG App</h1>
      <p className="text-lg mb-8">Upload documentation URL and chat with it using Gemini</p>
      <a 
        href="/upload" 
        className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg transition-colors"
      >
        Get Started
      </a>
    </div>
  );
}