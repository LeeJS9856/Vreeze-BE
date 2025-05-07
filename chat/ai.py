from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from django.conf import settings

class AIHelper:
    def __init__(self, session_id):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )

        # 세션별 대화 기억을 유지하기 위해 memory를 세션별 저장
        if session_id not in _advisor_instances:
            _advisor_instances[session_id] = {
                "memory": ConversationBufferMemory(
                    memory_key="chat_history",
                    return_messages=True
                )
            }
        
        self.memory = _advisor_instances[session_id]["memory"]

    def create_prompt(self, question, chat_history):
        """프롬프트 생성"""
        messages = [
            ("system", "당신은 질문자의 친한 친구일수도, 가족일수도 있습니다. 해당 입장에서 답변해주세요.")
        ]

        # 🔹 이전 대화 기록 추가
        for chat in chat_history:
            if isinstance(chat, HumanMessage):
                messages.append(("human", chat.content))
            elif isinstance(chat, AIMessage):
                messages.append(("assistant", chat.content))

        # 현재 질문 추가
        messages.append(("human", "{question}"))

        return ChatPromptTemplate.from_messages(messages)

    def generate_response(self, question):
        """최종 응답 생성"""
        # 1. 이전 대화 기록 가져오기
        chat_history = self.memory.load_memory_variables({}).get("chat_history", [])
        if chat_history is None:
            chat_history = []

        # 2. 프롬프트 생성
        prompt = self.create_prompt(question, chat_history)
        
        # 3. 체인 구성 및 실행
        chain = prompt | self.llm
        response = chain.invoke({"question": question})

        # 4. 대화 저장
        self.memory.save_context(
            {"input": question},
            {"output": str(response)}
        )
        
        return str(response)

# 인스턴스를 전역으로 유지
_advisor_instances = {}

# 메인 함수
def ai_chat(question, session_id):
    if session_id not in _advisor_instances:
        _advisor_instances[session_id] = AIHelper(session_id)
    
    advisor = _advisor_instances[session_id]
    response = advisor.generate_response(question)
    
    return response
