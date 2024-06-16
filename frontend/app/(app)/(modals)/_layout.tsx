import { Stack } from "expo-router";

export default function AppEntry() {
  return (
    <Stack>
      <Stack.Screen name="modal" options={{ headerShown: false }} />
      <Stack.Screen name="workout-modal" options={{ headerShown: false }} />
    </Stack>
  );
}