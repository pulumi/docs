/*
    This file includes the types for the PulumiAI API.
    The api expects messages in the following structure:

    {
        type: MessageType,
        data: {},
    }
*/

// The different ChatGPT models supported.
export type ChatGptModel = "gpt-4" | "gpt-3.5-turbo";


// The languages supported.
export enum Language {
    TYPESCRIPT = "TypeScript",
    PYTHON = "Python",
    GO = "Go",
    CSHARP = "C#",
}

export interface ConversationItem {
    conversationId: string;
    language: string;
    prompt: string;
    response: string;
    version: number;
    created: number;

    originalConversationId?: string;
}

// The types of messages supported.
export enum MessageType {
    // Messages
    PING ="PING",
    CREATE_CONNECTION = "CREATE_CONNECTION",
    GENERATE_NEW_OUTPUT = "GENERATE_NEW_OUTPUT",
    OUTPUT_CHUNK = "OUTPUT_CHUNK",
    OUTPUT_COMPLETE = "OUTPUT_COMPLETE",
    VERSION_FRIENDLY_TITLE = "VERSION_FRIENDLY_TITLE",
    SET_CONNECTION_USER_IDS = "SET_CONNECTION_USER_IDS",
    GET_CONVERSATION = "GET_CONVERSATION",
    SEND_FEEDBACK = "SEND_FEEDBACK",

    // Errors
    SERVER_ERROR = "SERVER_ERROR",
    OPENAI_RATE_LIMIT_ERROR = "OPENAI_RATE_LIMIT_ERROR",
    OVER_MESSAGE_LIMIT_ERROR = "OVER_MESSAGE_LIMIT_ERROR",
}

// Get Conversation
export interface GetConversationResponse {
    conversation: ConversationItem[];
}

export interface GetConversationArgs {
    conversationId: string;
}

// Ping
export interface PingResponse {
    ok: boolean;
}

export interface PingArgs {}
// Feedback
export interface FeedbackResponse {
    ok: boolean;
}

export interface FeedbackArgs {
    resultId: string;
    anonymousId: string;
    helpful: boolean;
    userId: string;
    comments?: string;
}

// Version Friendly Title
export interface VersionFriendlyTitleResponse {
    title: string;
    version: number;
}

// Set Connection user ids
export interface SetConnectionUserIdsArgs {
    segmentAnonymousId: string;
    pulumiUserId?: string;
}

// Create Connection
export interface CreateConnectionResponse {
    conversationId: string;
    authenticated: boolean;
    messageLimit?: number;
}

export interface CreateConnectionArgs {
    segmentAnonymousId: string;
    pulumiUserId?: string;
}

// Output Chunk
export interface OutputChunkResponse {
    order: number;
    content: string;
}

// Output Complete
export interface OutputCompleteResponse {
    ok: boolean;
}

// Generate New Output
export interface GenerateNewOutputArgs {
    conversationId: string;
    language: Language;
    instructions: string;
    program: string;
    model: ChatGptModel;
    version: number;

    originalConversationId?: string;
}

export interface GenerateNewOutputResponse {
    resultId: string;
    code: string;
    text: string;
}

// Server Error
export interface ServerErrorResponse {
    message: string;
}

// OpenAI Rate Limit error
export interface OpenAIRateLimitErrorResponse {
    message: string;
}

// Over Message Limit
export interface OverMessageLimitErrorResponse {
    message: string;
}

// PulumiGPTApiMessage represents the structure of an API message.
interface PulumiGPTApiMessage<M extends MessageType, D> {
    type: M;
    data: D;
}

// Actions
export type GenerateNewOutputAction = PulumiGPTApiMessage<MessageType.GENERATE_NEW_OUTPUT, GenerateNewOutputArgs>;
export type CreateConnectionAction = PulumiGPTApiMessage<MessageType.CREATE_CONNECTION, CreateConnectionArgs>;
export type SetConnectionUserIdsAction = PulumiGPTApiMessage<MessageType.SET_CONNECTION_USER_IDS, SetConnectionUserIdsArgs>;
export type GetConversationAction = PulumiGPTApiMessage<MessageType.GET_CONVERSATION, GetConversationArgs>;
export type SendFeedbackAction = PulumiGPTApiMessage<MessageType.SEND_FEEDBACK, FeedbackArgs>;

export type Action =
    GenerateNewOutputAction |
    CreateConnectionAction |
    SendFeedbackAction |
    GetConversationAction;

// Responses
export type OutputChunk = PulumiGPTApiMessage<MessageType.OUTPUT_CHUNK, OutputChunkResponse>;
export type OutputComplete = PulumiGPTApiMessage<MessageType.OUTPUT_COMPLETE, OutputCompleteResponse>;
export type GenerateNewOutput = PulumiGPTApiMessage<MessageType.GENERATE_NEW_OUTPUT, GenerateNewOutputResponse>;
export type ServerError = PulumiGPTApiMessage<MessageType.SERVER_ERROR, ServerErrorResponse>;
export type CreateConnection = PulumiGPTApiMessage<MessageType.CREATE_CONNECTION, CreateConnectionResponse>;
export type VersionTitle = PulumiGPTApiMessage<MessageType.VERSION_FRIENDLY_TITLE, VersionFriendlyTitleResponse>;
export type OpenAIRateLimit = PulumiGPTApiMessage<MessageType.OPENAI_RATE_LIMIT_ERROR, OpenAIRateLimitErrorResponse>;
export type OverMessageLimit = PulumiGPTApiMessage<MessageType.OVER_MESSAGE_LIMIT_ERROR, OverMessageLimitErrorResponse>;
export type Ping = PulumiGPTApiMessage<MessageType.PING, PingResponse>;
export type GetConversation = PulumiGPTApiMessage<MessageType.GET_CONVERSATION, GetConversationResponse>;
export type SendFeedback = PulumiGPTApiMessage<MessageType.SEND_FEEDBACK, FeedbackResponse>;

export type Response =
    GenerateNewOutput |
    ServerError |
    OutputChunk |
    OutputComplete |
    CreateConnection |
    VersionTitle |
    OpenAIRateLimit |
    OverMessageLimit | 
    Ping |
    GetConversation |
    SendFeedback;
