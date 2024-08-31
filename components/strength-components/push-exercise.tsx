import SelectDropdown from "react-native-select-dropdown";
import React, { FC } from "react";
import { View, Text } from "../Themed";
import { StyleSheet } from "react-native";

interface Props {
  setPushExercise: (type: string) => void;
}

const PushExercise: FC<Props> = ({ setPushExercise }) => {
  const options = [{ title: "Push ups" }, { title: "Dips" }, { title: "Bench press" }];

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Push:</Text>
      <SelectDropdown
        data={options}
        onSelect={(selectedItem) => {
          setPushExercise(selectedItem.title.toLowerCase());
        }}
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
  },
  dropdownButtonStyle: {
    margin: 10,
    width: 200,
    height: 40,
    backgroundColor: "#E9ECEF",
    // borderRadius: 12,
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
    // borderRadius: 8,
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

export default PushExercise;
