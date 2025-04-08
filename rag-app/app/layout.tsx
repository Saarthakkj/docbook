import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster"; // Assuming shadcn setup places components in @/components

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Documentation RAG App",
  description: "A NotebookLM-style RAG application for documentation",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main className="container mx-auto px-4 py-8">
          {children}
        </main>
        <Toaster /> {/* Add Toaster here */}
      </body>
    </html>
  );
}