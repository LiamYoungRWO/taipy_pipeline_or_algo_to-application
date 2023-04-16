# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from sqlalchemy import Column, Integer, Text

from ._sql_base_model import Base


class _TaipyModel(Base):  # type: ignore
    """_TaipyModel Represents the table used to store the information of taipy entities."""

    __tablename__ = "taipy_model"

    id = Column(Integer, primary_key=True)
    model_id = Column(Text)
    model_name = Column(Text)
    document = Column(Text)

    def __int__(self, model_id: str, model_name: str, document: str):
        self.model_id = model_id
        self.model_name = model_name
        self.document = document
