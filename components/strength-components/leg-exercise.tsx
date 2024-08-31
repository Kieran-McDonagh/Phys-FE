import SelectDropdown from "react-native-select-dropdown";
import React, { FC } from "react";
import { View, Text } from "@/components/Themed";
import { StyleSheet } from "react-native";
import WeightInput from "./weight-input";
import RepCounterList from "./rep-counter-list";

type props = {
  legExercise: string;
  setLegExercise: (legExercise: string) => void;
  legWeight: string;
  setLegWeight: (legWeight: string) => void;
  legSets: number[];
  setLegSets: (legSets: number[]) => void;
};

const LegExercise: FC<props> = ({
  legExercise,
  setLegExercise,
  legWeight,
  setLegWeight,
  legSets,
  setLegSets,
}) => {
  const options = [{ title: "Squats" }, { title: "Lunges" }, { title: "RDLs" }];

  const handleSelect = (selectedItem: { title: string }) => {
    setLegExercise(selectedItem.title.toLowerCase());
  };

  return (
    <>
      <View style={styles.container}>
        <Text style={styles.text}>Leg:</Text>
        <SelectDropdown
          data={options}
          onSelect={handleSelect}
          renderButton={(selectedItem) => (
            <View style={styles.dropdownButtonStyle}>
              <Text style={styles.dropdownButtonTxtStyle}>
                {(selectedItem && selectedItem.title) || "Not Selected"}
              </Text>
            </View>
          )}
          renderItem={(item, index, isSelected) => (
            <View style={[styles.dropdownItemStyle, isSelected && { backgroundColor: "#D2D9DF" }]}>
              <Text style={styles.dropdownItemTxtStyle}>{item.title}</Text>
            </View>
          )}
          showsVerticalScrollIndicator={false}
          dropdownStyle={styles.dropdownMenuStyle}
        />
        <WeightInput weight={legWeight} setWeight={setLegWeight} />
      </View>
      <RepCounterList sets={legSets} setSets={setLegSets} />
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 1,
  },
  dropdownButtonStyle: {
    margin: 10,
    width: 200,
    height: 40,
    backgroundColor: "#E9ECEF",
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 12,
  },
  dropdownButtonTxtStyle: {
    flex: 1,
    fontSize: 16,
    fontWeight: "500",
    color: "#151E26",
  },
  dropdownButtonArrowStyle: {
    fontSize: 28,
  },
  dropdownButtonIconStyle: {
    fontSize: 28,
    marginRight: 8,
  },
  dropdownMenuStyle: {
    backgroundColor: "#E9ECEF",
  },
  dropdownItemStyle: {
    width: "100%",
    flexDirection: "row",
    paddingHorizontal: 12,
    justifyContent: "center",
    alignItems: "center",
    paddingVertical: 8,
  },
  dropdownItemTxtStyle: {
    flex: 1,
    fontSize: 16,
    fontWeight: "500",
    color: "#151E26",
  },
  dropdownItemIconStyle: {
    fontSize: 28,
    marginRight: 8,
  },
  text: {
    fontSize: 16,
  },
});

export default LegExercise;
