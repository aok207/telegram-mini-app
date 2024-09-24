/* eslint-disable @typescript-eslint/no-explicit-any */
export interface ITelegramUser {
  id: number;
  first_name: string;
  last_name: string;
  username: string;
  language_code: string;
}

export interface IWebApp {
  initData: string;
  initDataUnsafe: {
    query_id: string;
    user: ITelegramUser;
    auth_date: string;
    hash: string;
  };
  version: string;
  platform: string;
  colorScheme: string;
  themeParams: {
    link_color: string;
    button_color: string;
    button_text_color: string;
    secondary_bg_color: string;
    hint_color: string;
    bg_color: string;
    text_color: string;
  };
  isExpanded: boolean;
  viewportHeight: number;
  viewportStableHeight: number;
  isClosingConfirmationEnabled: boolean;
  headerColor: string;
  backgroundColor: string;
  BackButton: {
    isVisible: boolean;
  };
  MainButton: {
    text: string;
    color: string;
    textColor: string;
    isVisible: boolean;
    isProgressVisible: boolean;
    isActive: boolean;
  };
  HapticFeedback: any;
}

export interface MetaData {
  title: string;
  description: string;
  author: string;
  published_date: string;
  og_img: string;
  og_type: string;
}

export interface Content {
  tag?: string;
  text?: string;
  img?: string;
  link?: string;
}

export interface Data {
  [url: string]: {
    page_type: string;
    meta_data: MetaData;
    contents: Content[];
  };
}

export interface ApiResponse {
  data?: Data[];
  error?: string;
}
