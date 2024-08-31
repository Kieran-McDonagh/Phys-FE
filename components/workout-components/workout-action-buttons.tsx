import { StyleSheet, TouchableOpacity } from "react-native";
import { View } from "../Themed";
import { AntDesign, Entypo } from "@expo/vector-icons";
import React, { FC } from "react";
import useUserStore from "@/store/userStore";
import useWorkoutStore from "@/store/workoutStore";

const WorkoutActionButtons: FC<{ id: string }> = ({ id }) => {
  const { user } = useUserStore();
  const { deleteWorkout } = useWorkoutStore();

  const handleDelete = async (workoutId: string) => {
    if (user) {
      const { access_token, token_type } = user;
      try {
        await deleteWorkout(workoutId, access_token, token_type);
      } catch (error) {
        console.error("Error deleting workout data:", error);
      }
    }
  };

  return (
    <View style={styles.actions}>
      <TouchableOpacity>
        <Entypo name="edit" size={24} color="black" />
      </TouchableOpacity>
      <TouchableOpacity
        onPress={() => {
          handleDelete(id);
        }}
      >
        <AntDesign name="delete" size={24} color="black" />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  actions: {
    display: "flex",
    flexDirection: "row",
    height: 30,
    gap: 20,
    backgroundColor: "pink",
  },
});

export default WorkoutActionButtons;
