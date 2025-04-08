/**
 * Chunks markdown text into smaller segments based on tokens
 */
export function chunkMarkdown(markdownText, maxTokens = 500) {
  if (!markdownText) return [];

  // Split by headings to create natural breaks
  const headingRegex = /(?=^#{1,6}\s.+$)/gm;
  let segments = markdownText.split(headingRegex);

  // Further split large segments
  const chunks = [];
  
  segments.forEach(segment => {
    // Estimate tokens - rough approximation (1 token ~= 4 chars)
    const estimatedTokens = segment.length / 4;
    
    if (estimatedTokens <= maxTokens) {
      chunks.push(segment.trim());
    } else {
      // Split by paragraphs for large segments
      const paragraphs = segment.split(/\n\s*\n/);
      let currentChunk = '';
      
      paragraphs.forEach(paragraph => {
        const paragraphTokens = paragraph.length / 4;
        
        if ((currentChunk.length / 4) + paragraphTokens <= maxTokens) {
          currentChunk += (currentChunk ? '\n\n' : '') + paragraph;
        } else {
          if (currentChunk) {
            chunks.push(currentChunk.trim());
          }
          
          // If a single paragraph is too large, split it further
          if (paragraphTokens > maxTokens) {
            const sentences = paragraph.split(/(?<=\.|\?|\!)\s+/);
            currentChunk = '';
            
            sentences.forEach(sentence => {
              const sentenceTokens = sentence.length / 4;
              
              if ((currentChunk.length / 4) + sentenceTokens <= maxTokens) {
                currentChunk += (currentChunk ? ' ' : '') + sentence;
              } else {
                if (currentChunk) {
                  chunks.push(currentChunk.trim());
                }
                currentChunk = sentence;
              }
            });
            
            if (currentChunk) {
              chunks.push(currentChunk.trim());
            }
          } else {
            currentChunk = paragraph;
          }
        }
      });
      
      if (currentChunk) {
        chunks.push(currentChunk.trim());
      }
    }
  });
  
  // Filter out any empty chunks
  return chunks.filter(chunk => chunk.trim().length > 0);
}