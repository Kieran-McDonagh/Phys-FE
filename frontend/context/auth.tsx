import {
  createContext,
  useContext,
  useEffect,
  useState,
  PropsWithChildren,
} from "react";
import { useRouter, useSegments } from "expo-router";

const AuthContext = createContext<any>(null);

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<string | null>(null);
  const segments = useSegments();
  const router = useRouter();

  useEffect(() => {
    if (!user && segments[0] !== "(auth)") {
      router.replace("/(auth)/login");
    } else if (user && segments[0] !== "(app)") {
      router.replace("/");
    }
  }, [user, segments]);

  return (
    <AuthContext.Provider
      value={{
        user,
        signIn: () => setUser("signed in"),
        signOut: () => setUser(null),
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}
