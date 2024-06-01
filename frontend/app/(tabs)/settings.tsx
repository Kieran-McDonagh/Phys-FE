import { View, Text, StyleSheet } from "react-native";
import { Link } from "expo-router";
import { ThemedText } from "@/components/ThemedText";

export default function Tab() {
  return (
    <View style={styles.container}>
      <Text>Settings Page</Text>
      <Link href="/">
        <ThemedText type="link">Press to go to home</ThemedText>
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
