import React, { useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

interface Props {
  setSelectedType: (type: string) => void;
}

const TypeChoice: React.FC<Props> = ({ setSelectedType }) => {
  const [selectedType, setSelectedTypeState] = useState<string | null>(null);

  const handlePress = (type: string) => {
    setSelectedType(type);
    setSelectedTypeState(type);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Type:</Text>
      <TouchableOpacity
        style={[styles.item, selectedType === "individual" && styles.selectedItem]}
        onPress={() => handlePress("individual")}
      >
        <Text style={styles.optionText}>Individual</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={[styles.item, selectedType === "battlephys" && styles.selectedItem]}
        onPress={() => handlePress("battlephys")}
      >
        <Text style={styles.optionText}>Battlephys</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    gap: 10,
    alignItems: "center",
    justifyContent: "center",
    borderWidth: 1,
    borderColor: "red",
  },
  item: {
    paddingVertical: 10,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    backgroundColor: "#f9f9f9",
    borderRadius: 5,
  },
  selectedItem: {
    backgroundColor: "#add8e6",
  },
  optionText: {
    fontSize: 16,
  },
  text: {
    fontSize: 16,
    color: "white",
    borderWidth: 1,
    borderColor: "red",
    width: "15%"

  },
});

export default TypeChoice;
