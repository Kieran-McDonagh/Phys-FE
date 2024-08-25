import { create } from "zustand";
import sendLoginData from "@/api/login";
import sendRegisterData from "@/api/register";

interface UserData {
  id: string;
  username: string;
  full_name: string;
  email: string;
  disabled: boolean;
  workouts: any[];
  friends: any[];
}

interface User {
  access_token: string;
  token_type: string;
  user_data: UserData;
}

interface UserState {
  user: User | null;
  signIn: (username: string, password: string) => Promise<void>;
  registerUser: (email: string, username: string, full_name: string, password: string) => Promise<void>;
  signOut: () => void;
}

const useUserStore = create<UserState>((set, get) => ({
  user: null,
  signIn: async (username: string, password: string) => {
    try {
      const response = await sendLoginData(username, password);
      set({ user: response });
    } catch (error) {
      console.error("Login failed:", error);
      throw error;
    }
  },
  registerUser: async (email: string, username: string, full_name: string, password: string) => {
    try {
      await sendRegisterData(email, username, full_name, password);
      await get().signIn(username, password);
    } catch (error) {
      console.error("Registration failed:", error);
      throw error;
    }
  },
  signOut: () => {
    set({ user: null });
  },
}));

export default useUserStore;
