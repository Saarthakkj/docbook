from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import MarkdownifyTransformer
from bs4 import BeautifulSoup

urls = ["https://docs.crawl4ai.com/"]
loader = AsyncHtmlLoader(urls)
docs = loader.load()
print(docs)
md = MarkdownifyTransformer()
converted_docs = md.transform_documents(docs)
print("\n\n\n --- converted-- ")
print(converted_docs[0].page_content[:1000])
# Assuming docs contains your HTML content
print("\n\n --- docs page content ---")
#print(docs[0].page_content)
print("\n\n ----- docs title ---")
#print(docs[0].title)
soup = BeautifulSoup(docs[0].page_content, 'html.parser')

# Now you can navigate through tags
# For example, to find all links:
print("\n\n\n --- only links ---")
for link in soup.find_all('a'):
    print(link.get('href'))  # Prints the URL of each link



#only_links = MarkdownifyTransformer(strip=[ "a.href"])
#converted_docs =  md.transform_documents(docs)
#print("\n\n\n --- only links---")
#print(converted_docs[0].page_content[:1000])


