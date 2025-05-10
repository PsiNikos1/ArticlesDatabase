from flask import request, jsonify

from initializer._init_ import db
from model.Tag import Tag


class TagController:

    def get_all_tags(self):
        """
        Get all tags
        :return:
        """
        print("hi")
        tags = Tag.query.all()
        return [tag.to_dict() for  tag in tags]

    def create_tag(self):
        """
        Create a tag on an article
        :return: 
        """
        data = request.json
        new_tag = Tag(content=data["content"])
        db.session.add(new_tag)
        db.session.commit()

        return jsonify({"message": "Tag created", "id": new_tag.id}), 201


    def delete_tag(self):
       """
        Delete a tag from the article
       :param tag_id:
       :return:
       """
       data = request.json
       tag_id = data.get("id")
       tag = Tag.query.get_or_404(tag_id)
       db.session.delete(tag)
       db.session.commit()
       return jsonify({"message": f"Tag with id {tag.id} deleted"})

    def update_tag(self):
        data = request.json
        tag = Tag.query.get_or_404(data["id"])

        new_content = data.get("content")
        if not new_content:
            return jsonify({"error": "Missing 'name' field"}), 400

        tag.content = new_content
        db.session.commit()

        return jsonify({"message": "Tag updated"}), 204