import requests
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ResearchPaper(Base):
    __tablename__ = 'research_papers'
    id = Column(String, primary_key=True)
    title = Column(String)
    authors = Column(String)
    abstract = Column(String)
    url = Column(String)


def fetchResearchPapers(topic):
    api_key = 'g5nxrz29ma3rcpntqrsfd47a'
    url = f'http://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=altmetrics&format=json&apikey=g5nxrz29ma3rcpntqrsfd47a'

    response = requests.get(url)
    data = response.json()

    return data['results']


def storeResearchPapers(papers):
    engine = create_engine('database://myuser:mypassword@localhost:3306/mydatabase')
    Session = sessionmaker(bind=engine)
    session = Session()

    for paper in papers:
        research_paper = ResearchPaper(
            id=paper['id'],
            title=paper['title'],
            authors=paper['authors'],
            abstract=paper['abstract'],
            url=paper['url']
        )
        session.add(research_paper)

    session.commit()
    session.close()


