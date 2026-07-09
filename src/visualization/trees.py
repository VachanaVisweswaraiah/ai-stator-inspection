def serialize_decision_tree(model, feature_names, class_labels):
    def serialize_node(node_id):
        is_leaf = model.tree_.feature[node_id] == -2
        if is_leaf:
            values = model.tree_.value[node_id][0]
            predicted_class = model.classes_[values.argmax()]
            return {
                "id": node_id,
                "type": "leaf",
                "prediction": class_labels.get(
                    predicted_class,
                    "Unknown",
                ),
                "samples": int(sum(values)),
                "class_distribution": values.tolist(),
            }

        feature = feature_names[model.tree_.feature[node_id]]
        left_id = model.tree_.children_left[node_id]
        right_id = model.tree_.children_right[node_id]
        return {
            "id": node_id,
            "type": "split",
            "feature": feature,
            "threshold": model.tree_.threshold[node_id],
            "left": serialize_node(left_id),
            "right": serialize_node(right_id),
        }

    return serialize_node(0)


__all__ = ["serialize_decision_tree"]
