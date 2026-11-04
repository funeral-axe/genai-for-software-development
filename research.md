# Research on Generative AI Applications

# 1. Offline AI Meeting Assistant

## Description

Currently, most companies hold meetings where employees discuss tasks and responsibilities. After the meeting, everyone goes back to work, tasks are assigned, and an hour later many details are already forgotten. It can also become unclear who is responsible for each task.

This is where an offline AI meeting assistant can help. The application records the meeting and uses AI to transcribe speech into text offline and perform speaker diarization. As a result, users receive a structured meeting report with the date, participants, assigned tasks, and responsible people.

## Business Value

This solution is useful because it requires minimal human involvement and automates meeting documentation. One of its main advantages is the ability to generate and download a detailed meeting report within seconds. If the application runs offline, employees can safely discuss sensitive or even confidential information during the meeting.

## Technical Challenges

One of the key technical challenges is recognizing mixed-language speech, when participants switch between different languages during the same conversation. This is common in many post-Soviet countries. Another challenge is speaker diarization, which means identifying who is speaking. Processing large audio files quickly will also require more powerful hardware. Noise reduction will be another important challenge.

## Weak Points

If several participants speak at the same time, the application may incorrectly recognize their speech or mix information from different speakers. Speaker diarization can also make mistakes and assign a phrase to the wrong participant.

Another weak point is hallucination. The AI model may generate incorrect information in the final report, for example, add a task that was not actually assigned during the meeting. Because of this, important meeting reports may still require human verification.

## Existing Implementations

- **Otter.ai** — [Official Website](https://otter.ai/)
  An AI meeting assistant that can record meetings, transcribe conversations, and automatically create meeting summaries.

- **Notion AI Meeting Notes** — [Official Website](https://www.notion.com/product/ai)
  A Notion AI feature that can transcribe meetings, summarize key points, and keep meeting information inside a workspace.

---

# 2. AI Personal Health Records Organizer

## Description

People often receive medical test results from different hospitals and laboratories. These results can be stored as paper documents, photos, PDF files, or in different medical applications. After some time, it becomes difficult to find an old result or understand how a medical indicator has changed.

An AI Personal Health Records Organizer can help solve this problem. A user can upload a photo, scan, or PDF with medical test results. The application can extract values from the document, recognize medical indicators and store them in a structured form. It can also show how these indicators change over time and generate a short summary of the user's medical records.

## Business Value

The main value of this solution is that users can keep their medical information in one place instead of searching through many documents and applications. It can also reduce manual data entry because information from medical reports can be extracted automatically.

Another benefit is the ability to see the history of medical indicators and their changes over time. This information can also be useful before a visit to a doctor because the user can quickly find previous results and prepare them for review.

## Technical Challenges

One of the main technical challenges is extracting correct information from different medical documents. Laboratories may use different document formats, measurement units, names, and reference ranges. Poor photo quality can also make OCR and data extraction more difficult.

Another challenge is data normalization. The application must understand when two differently formatted results represent the same medical indicator. Privacy and security are also important because medical records contain very sensitive personal information.

## Weak Points

OCR can incorrectly recognize numbers or measurement units. For example, one incorrectly recognized digit can completely change a medical test result. AI can also incorrectly interpret extracted information or generate a wrong summary.

Because this application works with medical information, users should not use its AI-generated summaries as a medical diagnosis. Important information should be verified, and medical decisions should still be made with a qualified medical professional.

## Existing Implementations

- **Apple Health** — [Official Website](https://www.apple.com/health/)
  Apple Health can collect health information and medical records, including laboratory results, and keep this information in one place.

- **HealthLab** — [App Store](https://apps.apple.com/kz/app/healthlab-blood-test-results/id6759285729)
  An application that uses AI to extract biomarkers, values, units, and reference ranges from photos and PDF laboratory reports and display their history as charts.

---

# 3. AI Personal Document & Knowledge Assistant

## Description

People and companies store a large number of documents, such as contracts, instructions, reports, invoices, and other files. Finding specific information inside these documents can take a lot of time, especially when the user does not remember the exact file name or location.

An AI Personal Document & Knowledge Assistant can allow users to upload documents and ask questions using natural language. For example, a user can ask, "When does my contract expire?" instead of manually searching through the whole document. The AI can find relevant information in available documents and generate an answer based on them.

## Business Value

The main business value is saving time when searching for information. Employees can receive information from company documents faster without manually opening many files.

This solution can also make company knowledge easier to access. New employees can find information about company processes, documentation, and rules without asking other employees every time.

## Technical Challenges

One technical challenge is processing many different document formats. Some files may contain normal text, while others can contain scanned pages that require OCR.

Another challenge is finding the correct information for the user's question. Technologies such as RAG, embeddings, and vector search can be used for this purpose. The system also needs to respect access permissions so that users cannot receive information from documents they are not allowed to access.

## Weak Points

The AI can retrieve an irrelevant document or miss an important part of the information. If incorrect context is provided to the model, the generated answer can also be incorrect.

Another problem is outdated information. If old and new versions of the same document exist in the system, the AI may use the wrong version. Sensitive documents also require strong access control and data protection.

## Existing Implementations

- **Gemini Notebook** — [Official Website](https://workspace.google.com/products/gemini-notebook/)
  An AI research and knowledge assistant that can work with uploaded PDFs, documents, websites, audio files, and other sources.

- **Notion AI Enterprise Search** — [Official Website](https://www.notion.com/product/enterprise-search)
  An AI search system that can find information across a Notion workspace and connected applications and answer questions using this information.

---

# 4. AI Software Maintenance Assistant

## Description

Software developers often need to work with large projects that contain thousands of files and code written by other developers. Understanding an unfamiliar project can take a lot of time, especially when the project is old and has limited documentation.

An AI Software Maintenance Assistant can analyze the project and help developers understand existing code. Developers can ask questions about the codebase, generate tests, find possible bugs, explain functions, and receive suggestions for code changes.

## Business Value

This solution can increase developer productivity and reduce time spent on repetitive work. It can also help new developers understand an unfamiliar project faster.

AI can help with code explanation, test generation, debugging, and simple code changes. Developers can spend more time on complex tasks instead of manually searching through a large codebase.

## Technical Challenges

Large software projects may contain more code than an AI model can process at one time because models have context window limitations. Because of this, the system needs to find and provide only relevant parts of the project to the model.

Another challenge is understanding dependencies between different parts of the application. Security is also important because company source code may contain confidential information and should not be sent to unauthorized external services.

## Weak Points

AI can generate code that looks correct but contains logical errors or security vulnerabilities. It can also hallucinate functions, libraries, or APIs that do not exist.

The model may not fully understand the business logic of a large application. Because of this, AI-generated code should still be reviewed and tested by developers before it is added to the project.

## Existing Implementations

- **GitHub Copilot** — [Official Website](https://github.com/features/copilot)
  An AI coding assistant that can use repository context to help developers write, understand, review, and modify software.

- **Amazon Q Developer** — [Official Website](https://aws.amazon.com/q/developer/)
  A generative AI assistant for software development that can help developers work with code from IDEs and other development tools.

---

# 5. AI Customer Request and Ticket Processing

## Description

Companies can receive hundreds or thousands of customer requests through email, chats, and support systems. Employees need to read these messages, understand the problem, find the necessary information, and prepare a response. This can take a lot of time when the number of customers is large.

An AI Customer Request and Ticket Processing system can automatically analyze incoming requests, classify them, find information in the company's knowledge base, and generate a possible response. Simple requests can be processed automatically, while more complex requests can be sent to a human employee.

## Business Value

The main business value is faster customer support. AI can process simple and repetitive requests automatically and reduce the amount of manual work for support employees.

This also allows a company to process more requests without increasing the support team at the same rate. Employees can focus on difficult cases while AI handles common questions.

## Technical Challenges

The system needs to correctly understand and classify different customer requests. It also needs access to current company information to generate useful answers. RAG can be used to find relevant information from the company's knowledge base before generating a response.

Integration with existing ticket systems can also be difficult. Customer requests may contain personal or confidential data, so privacy and access control must also be considered.

## Weak Points

AI can incorrectly classify a request or generate an incorrect answer. Another problem can appear when the company's knowledge base contains outdated information.

Some requests can also be too sensitive or complicated for automatic processing. In these cases, a human employee should verify the AI response or take control of the conversation.

## Existing Implementations

- **Fin AI Agent** — [Official Website](https://www.intercom.com/fin)
  An AI customer service agent that can use company support content to answer customer questions and handle requests across different communication channels.

- **Zendesk AI** — [Official Website](https://www.zendesk.com/service/ai/)
  An AI solution for customer service that helps automate support requests and assist customer service teams.

---

# Conclusion

These five use cases show that Generative AI can be used in very different areas, from meetings and personal documents to healthcare, software development, and customer support. In most cases, the main business value is similar: AI can automate repetitive tasks, save time, and help people work with large amounts of information faster.

At the same time, these applications have similar problems. AI can hallucinate, misunderstand information, or generate incorrect results. Privacy and security are also important when the system works with confidential, medical, company, or customer data. For this reason, human verification is still important in situations where an AI error can have serious consequences.

For me, the Offline AI Meeting Assistant and AI Personal Health Records Organizer are the most interesting use cases because they solve problems that I can see in real life and can potentially be implemented as complete applications.