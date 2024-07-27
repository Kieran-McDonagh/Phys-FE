import { useEffect, PropsWithChildren } from "react";
import { useRouter, useSegments } from "expo-router";
import useUserStore from "@/store/userStore";

export function AuthProvider({ children }: PropsWithChildren<{}>) {
  const { user } = useUserStore();
  const segments = useSegments();
  const router = useRouter();

  useEffect(() => {
    if (!user && segments[0] !== "(auth)") {
      router.replace("/(auth)/login");
    } else if (user && segments[0] !== "(app)") {
      router.replace("/");
    }
  }, [user, segments]);

  return <>{children}</>; 
}

