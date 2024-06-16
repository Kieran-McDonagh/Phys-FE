import { StyleSheet, Text, TextInput, View } from "react-native";

interface Props {
  title: string;
  setTitle: (type: string) => void;
}

const WorkoutTitle: React.FC<Props> = ({ title, setTitle }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Title:</Text>
      <TextInput style={styles.input} onChangeText={setTitle} value={title} autoCapitalize="none" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    gap: 10,
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 1,
    borderColor: "red",
  },
  text: {
    fontSize: 16,
    color: "white",
    borderWidth: 1,
    borderColor: "red",
    width: "15%"

  },
  input: {
    backgroundColor: "white",
    height: 40,
    borderWidth: 1,
    padding: 10,
    width: "70%",
    textAlign: "center",
  },
});

export default WorkoutTitle;
