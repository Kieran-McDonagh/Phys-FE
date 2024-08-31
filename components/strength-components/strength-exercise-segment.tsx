import React, { FC } from "react";
import { Text, View } from "../Themed";
import { StyleSheet } from "react-native";

type exerciseData = {
  exercise: string;
  weight: string;
  sets: number[];
};

interface Props {
  exercise: exerciseData;
}

const ExerciseSegment: FC<Props> = ({ exercise }) => {
  return (
    <View style={styles.container}>
      <View style={styles.exerciseAndWeight}>
        <Text style={styles.exerciseText}>{exercise.exercise}</Text>
        <Text style={styles.weightText}>{exercise.weight}</Text>
      </View>
      <View style={styles.sets}>
        {exercise.sets
          .filter((set) => set !== 0)
          .map((set, index) => (
            <Text key={index} style={styles.text}>
              Set {index + 1}: {set}
            </Text>
          ))}
      </View>
    </View>
  );
};

export default ExerciseSegment;

const styles = StyleSheet.create({
  container: {
    backgroundColor: "pink",
  },
  exerciseAndWeight: {
    backgroundColor: "pink",
    display: "flex",
    flexDirection: "row",
    alignContent: "center",
    alignItems: "center",
  },
  sets: {
    backgroundColor: "pink",
    display: "flex",
    flexWrap: "wrap",
    flexDirection: "row",
    justifyContent: "flex-start",
    gap: 10,
    margin: 10,
    width: "80%",
  },
  exerciseText: {
    fontSize: 30,
    color: "black",
    marginHorizontal: 10,
  },
  weightText: {
    fontSize: 25,
    color: "black",
    marginHorizontal: 10,
  },
  text: {
    fontSize: 20,
    color: "black",
  },
});
