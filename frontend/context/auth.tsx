import { createContext, useContext, useEffect, useState, PropsWithChildren } from "react";
import { useRouter, useSegments } from "expo-router";
import sendLoginData from "@/api/login";
import sendRegisterData from "@/api/register";

interface User {
  id: string;
  username: string;
  full_name: string;
  email: string;
  disabled: boolean;
  workouts: any[];
  nutrition: any[];
  friends: any[];
}

interface AuthContextType {
  user: User | null;
  signIn: (username: string, password: string) => Promise<void>;
  registerUser: (email: string, username: string, full_name: string, password: string) => Promise<void>;
  signOut: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }: PropsWithChildren<{}>) {
  const [user, setUser] = useState<User | null>(null);
  const segments = useSegments();
  const router = useRouter();

  useEffect(() => {
    if (!user && segments[0] !== "(auth)") {
      router.replace("/(auth)/login");
    } else if (user && segments[0] !== "(app)") {
      router.replace("/");
    }
  }, [user, segments]);

  const signIn = async (username: string, password: string) => {
    try {
      const response = await sendLoginData(username, password);
      setUser(response.user_data);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const registerUser = async (email: string, username: string, full_name: string, password: string) => {
    try {
      await sendRegisterData(email, username, full_name, password);
      signIn(username, password);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const signOut = () => {
    setUser(null);
  };

  return <AuthContext.Provider value={{ user, signIn, registerUser, signOut }}>{children}</AuthContext.Provider>;
}
