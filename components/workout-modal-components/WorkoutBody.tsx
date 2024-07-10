import { StyleSheet, Text, TextInput, View } from "react-native";

interface Props {
  index: number;
  bodyKey: string;
  bodyValue: string;
  updateField: (index: number, key: string, value: string) => void;
}

const WorkoutBody: React.FC<Props> = ({ index, bodyKey, bodyValue, updateField }) => {
  const handleKeyChange = (key) => {
    updateField(index, key, bodyValue);
  };

  const handleValueChange = (value) => {
    updateField(index, bodyKey, value);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Body:</Text>
      <TextInput
        style={styles.input1}
        onChangeText={handleKeyChange}
        value={bodyKey}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input2}
        onChangeText={handleValueChange}
        value={bodyValue}
        autoCapitalize="none"
      />
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
    width: "15%",
  },
  input1: {
    backgroundColor: "white",
    height: 40,
    borderWidth: 1,
    padding: 10,
    width: "55%",
    textAlign: "center",
  },
  input2: {
    backgroundColor: "white",
    height: 40,
    borderWidth: 1,
    padding: 10,
    width: "12%",
    textAlign: "center",
  },
});

export default WorkoutBody;
