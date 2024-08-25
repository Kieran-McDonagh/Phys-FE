import React from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { AntDesign } from "@expo/vector-icons";
import { Entypo } from "@expo/vector-icons";
import useUserStore from "@/store/userStore";
import useWorkoutStore from "@/store/workoutStore";

interface Props {
  allWorkouts: any[];
}

const AllWorkouts: React.FC<Props> = ({ allWorkouts }) => {
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
    <ScrollView contentContainerStyle={styles.container}>
      {allWorkouts.map((workout, index) => (
        <View key={index} style={styles.item}>
          <View key={index} style={styles.actions}>
            <TouchableOpacity>
              <Entypo name="edit" size={24} color="black" />
            </TouchableOpacity>
            <TouchableOpacity
              onPress={() => {
                handleDelete(workout.id);
              }}
            >
              <AntDesign name="delete" size={24} color="black" />
            </TouchableOpacity>
          </View>
          <Text>Type: {workout.type}</Text>
          <Text>Notes: {workout.notes}</Text>
          <Text>User ID: {workout.user_id}</Text>
          <Text>Date Created: {workout.date_created}</Text>
          <Text>Body: {JSON.stringify(workout.body, null, 2)}</Text>
        </View>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  item: {
    paddingVertical: 10,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    marginBottom: 10,
    backgroundColor: "#f9f9f9",
    borderRadius: 5,
  },
  text: {
    fontSize: 16,
  },
  actions: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "flex-end",
    gap: 10,
  },
});

export default AllWorkouts;
