import { Stack } from "expo-router";
import React from "react";

export default function AppEntry() {
  return (
    <Stack>
      <Stack.Screen name="modal" options={{ headerShown: false }} />
      <Stack.Screen name="StrengthModal" options={{ headerShown: false }} />
      <Stack.Screen name="CardioModal" options={{ headerShown: false }} />
    </Stack>
  );
}
