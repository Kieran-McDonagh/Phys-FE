import { Stack } from "expo-router";
import React from "react";

export default function AppEntry() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false, headerBackTitle: "Back" }} />
      <Stack.Screen
        name="(modals)"
        options={{ presentation: "modal", headerShown: false, headerBackTitle: "Back" }}
      />
    </Stack>
  );
}
