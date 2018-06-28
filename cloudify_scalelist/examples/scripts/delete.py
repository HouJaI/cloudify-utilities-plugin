#!/usr/bin/env python
#
# Copyright (c) 2018 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs


if __name__ == '__main__':
    properties = {}
    # use properties provided by install
    properties.update(ctx.node.properties)
    # use properties provided by runtime_propoerties from other instances
    properties.update(inputs)
    # use properties provided by current node
    properties.update(ctx.instance.runtime_properties)
    ctx.logger.info("Resulted properties: {}".format(properties))

    if properties.get("resource_id"):
        ctx.logger.info("We have some resource {}, so we can delete such"
                        .format(repr(properties["resource_id"])))
        ctx.instance.runtime_properties["resource_id"] = None
    else:
        ctx.logger.info("Not fully created instances, skip it")