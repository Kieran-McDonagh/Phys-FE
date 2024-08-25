import { StyleSheet, ScrollView, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import React from "react";
import { Link } from "expo-router";

export default function TabOneScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Select type of workout</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Link style={[styles.pressable, styles.cardio]} href="/CardioModal" asChild>
          <TouchableOpacity>
            <Text style={styles.pressableText}>Cardio</Text>
          </TouchableOpacity>
        </Link>
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
        <Link style={[styles.pressable, styles.strength]} href="/StrengthModal" asChild>
          <TouchableOpacity>
            <Text style={styles.pressableText}>Strength & Conditioning</Text>
          </TouchableOpacity>
        </Link>
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
  scrollContent: {
    alignItems: "center",
    justifyContent: "center",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  pressable: {
    backgroundColor: "blue",
    margin: 10,
    padding: 50,
    width: "100%",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 10,
  },
  pressableText: {
    fontSize: 20,
    color: "black",
  },
  cardio: {
    backgroundColor: "blue",
  },
  strength: {
    backgroundColor: "red",
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold'
  }
});
