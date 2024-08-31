import React, { FC } from "react";
import { Text, View } from "../Themed";
import { StyleSheet, TouchableOpacity } from "react-native";
import RepCounter from "./rep-counter";

interface Props {
  sets: number[];
  setSets: (sets: number[]) => void;
}

const RepCounterList: FC<Props> = ({ sets, setSets }) => {
  const handleSetCountChange = (index: number, count: number) => {
    const updatedSets = [...sets];
    updatedSets[index] = count;
    setSets(updatedSets);
  };

  const handleReset = () => {
    setSets([0, 0, 0, 0, 0]);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Reps:</Text>
      {sets.map((count, index) => (
        <RepCounter key={index} index={index} count={count} setCount={handleSetCountChange} />
      ))}
      <TouchableOpacity onPress={handleReset}>
        <Text>reset</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    display: "flex",
    flexDirection: "row",
    gap: 10,
    justifyContent: "center",
    alignContent: "center",
    alignItems: "center",
    marginStart: 20,
  },
  text: {
    color: "white",
    fontSize: 16,
  },
});

export default RepCounterList;
