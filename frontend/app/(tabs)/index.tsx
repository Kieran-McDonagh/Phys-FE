import { View, Text, StyleSheet } from "react-native";
import { Link } from "expo-router";
import { ThemedText } from "@/components/ThemedText";

export default function Tab() {
  return (
    <View style={styles.container}>
      <Text>Home Page</Text>
      <Link href="/settings">
        <ThemedText type="link">Press to go to settings</ThemedText>
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
