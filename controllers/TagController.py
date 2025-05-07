from model.Tag import Tag


class TagController:

    def get_all_tags(self):
        """
        Get all tags
        :return:
        """
        tags = Tag.query.all()
        return [tag.to_dict() for  tag in tags]

    def create_tag(self):"""
        Create a tag on an article
        :return: 
        """


    def get_all_tags(self):
        """
        Get all tags on a specific article
        :return:
        """

    def delete_tag(self, tag_id):
       """
        Delete a tag from the article
       :param tag_id:
       :return:
       """