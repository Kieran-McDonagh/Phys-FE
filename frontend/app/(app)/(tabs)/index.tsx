import { StyleSheet, Button, ScrollView } from "react-native";
import { Text, View } from "@/components/Themed";
import { useAuth } from "@/context/auth";

export default function TabOneScreen() {
  const auth = useAuth();

  if (!auth) {
    return <Text>Loading...</Text>;
  }

  const { signOut, user } = auth;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>User Information</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

      <ScrollView style={styles.userInfo}>
        {user &&
          Object.entries(user).map(([key, value]) => (
            <View key={key} style={styles.userItem}>
              <Text style={styles.userKey}>{key}</Text>
              <Text style={styles.userValue}>{value}</Text>
            </View>
          ))}
      </ScrollView>

      <Button title="Sign-out" color={"yellow"} onPress={signOut} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 16,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  userInfo: {
    width: "100%",
  },
  userItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  userKey: {
    fontWeight: "bold",
  },
  userValue: {
    marginLeft: 8,
  },
});
