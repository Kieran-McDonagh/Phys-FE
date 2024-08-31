import { Stack } from "expo-router";
import React from "react";

export default function AppEntry() {
  return (
    <Stack>
      <Stack.Screen name="modal" options={{ headerShown: false }} />
      <Stack.Screen name="StrengthModal" options={{ headerShown: true, headerBackTitle: "Back", headerTitle: "" }} />
      <Stack.Screen name="CardioModal" options={{ headerShown: true, headerBackTitle: "Back", headerTitle: "" }} />
    </Stack>
  );
}
