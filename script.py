from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import MarkdownifyTransformer
from bs4 import BeautifulSoup
import asyncio

def r_fn(url , stop , links , final_docs):
    if (stop > 1) : return 
    print(f"\n\n --- STOP :{stop}")
    j = 1
    docs = ""
    while(j <5 and docs == ""): 
        loader = AsyncHtmlLoader(url)
        docs = loader.load()
        j+=1
    #print(docs)
    if(docs == ""): return 
    md = MarkdownifyTransformer()
    converted_docs = md.transform_documents(docs)
    try : 
        final_docs.append(converted_docs[0].page_content[:1000])
        print("\n\n---- converted docs")
        print(converted_docs[0].page_content[1000])
    except :
        print("nothign worthwhile")
   # Assuming docs contains your HTML content
    #print("\n\n --- docs page content ---")
    #print(docs[0].page_content)
    #print("\n\n ----- docs title ---")
    #print(docs[0].title)

    soup = BeautifulSoup(docs[0].page_content, 'html.parser')

    # Now you can navigate through tags
    # For example, to find all links:
    #print("\n\n\n --- only links ---")
    
    
    for link in soup.find_all('a'):
        links.append(link.get('href'))  # Prints the URL of each link
        print(f"\n\n ---LINK : {link.get('href')}")
        try:
            r_fn(link.get('href') , stop+1 , links)
        except : 
            print("error fetching" , link.get('href'))
            try: 
                loader = AsyncHtmlLoader(link.get('href'))
                docs = loader.load()
            except : 
                print("fault in url")

            


    

i = 50
url = 'https://www.aliexpress.us/item/3256802994929985.html?gatewayAdapt=glo2usa4itemAdapt'
final_docs = []
links = []
r_fn(url , 0 , links , final_docs)

print(links)
print("\n\n")
print(final_docs)
#only_links = MarkdownifyTransformer(strip=[ "a.href"])
#converted_docs =  md.transform_documents(docs)
#print("\n\n\n --- only links---")
#print(converted_docs[0].page_content[:1000])


