import { StyleSheet, ScrollView } from "react-native";
import { Text, View } from "@/components/Themed";
import useUserStore from "@/store/userStore";

export default function TabOneScreen() {
  const { user } = useUserStore();

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Nutrition home page</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

      <ScrollView>
        <View>
          <Text>Nutrition data</Text>
        </View>
      </ScrollView>
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
});
