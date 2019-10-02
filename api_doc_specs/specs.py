'''
test: https://github.com/flasgger/flasgger
'''

user_get = {
"tags": [
    "users"
  ],
   "parameters": [
    {
      "name": "user_email",
      "in": "path",
      "type": "string",
      "required": True,
      "default": "mcole18@asu.edu",
      "description": "Which user do you want?"
    }
  ],
  "responses": {
    "200": {
      "description": "A user's public information",
      "schema": {
        "$ref": "#/definitions/User"
      },
      "examples": {
        "User" : {
      	 "Email": "test@donut.derp",
 		     "Favorite_Color": "FF8017",
 		     "Favorite_Hobby": "Pancakes",
 		     "Field": "Software Engineering",
 		     "Name": "Jacob Wallert",
 		     "Nametag": "test@donut.derp.nametag",
 		     "Superpower": "Overthinking"
 		}
 		}
    }
  }
}


user_put = {
  "tags": [
    "users"
  ],
  "definitions": {
    "User": {
      "type": "object",
      "properties": {
        "Email": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Favorite_Color": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Favorite_Hobby": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Field": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Name": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Nametag": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        },
        "Superpower": {
          "type": "string",
          "items": {
            "$ref": "#/definitions/User"
          }
        }
      }
    },
    "Name": {
      "type": "string"
    },
    "Email": {
      "type": "string"
    },
    "Favorite_Color": {
      "type": "string"
    },
    "Power": {
      "type": "string"
    },
    "Field": {
      "type": "string"
    },
    "Favorite_Hobby": {
      "type": "string"
    }
  },
  "parameters": [
    {
      "name": "body",
      "in": "body",
      "required": True,
      "schema": {
        "id": "User",
        "required": [
          "Email",
          "Favorite_Color",
          "Favorite_Hobby",
          "Field",
          "Name",
          "Superpower"
        ],
        "properties": {
          "Email": {
            "type": "string",
            "description": "The user's email.",
            "default": "mcole18@asu.edu"
          },
          "Favorite_Color": {
            "type": "string",
            "description": "The user's favorite color.",
            "default": "Green."
          },
          "Favorite_Hobby": {
            "type": "string",
            "description": "The user's favorite hobby.",
            "default": "Dance battles."
          },
          "Field": {
            "type": "string",
            "description": "The user's occupational/study field.",
            "default": "Software Engineering."
          },
          "Name": {
            "type": "string",
            "description": "The user's name.",
            "default": "Mason Cole."
          },
          "Superpower": {
            "type": "string",
            "description": "The user's superpower (real or imaginary).",
            "default": "Teleportation."
          }
        }
      }
    }
  ],
  "responses": {
    "200": {
      "description": "A single user item",
      "schema": {
        "$ref": "#/definitions/User"
      }
    }
  }
}


sponsor_get = {
"tags": [
    "sponsors"
  ],
  "parameters": [
    {
      "name": "sponsor_name",
      "in": "path",
      "type": "string",
      "required": True,
      "default": "GoDaddy",
      "description": "Which Sponsor info do you want?"
    }
  ],
  "responses": {
    "200": {
      "description": "A sponsor's public information",
      "schema": {
        "$ref": "#/definitions/Sponsor"
      },
      "examples": {
        "Sponsor" : {
        'Mission': 'GoDaddys vision and mission is to radically shift the global '
            'economy toward life-fulfilling independent ventures. We do that '
            'by helping our customers kick ass-giving them the tools, insights '
            'and the people to transform their ideas and personal initiative '
            'into success, however they measure it.',
            'Name': 'GoDaddy',
            'Recruiting': ['Software Engineering',
                'Engineering Management',
                'Data Science'],
            'Rep': 'Jane Smith',
            'Rep Field': 'Software Engineer'}
    }
    }
  }
}

meta_swag = {
    "swagger_version": "2.0",
    "title": "WARU",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "0.0.1",
            "title": "WARU RESTish API",
            "endpoint": 'v1_spec',
            "description": "Hey we use JSON so it\'s RESTish =]",
            "route": '/v1/spec',
            # # rule_filter is optional
            # # it is a callable to filter the views to extract
            # "rule_filter": lambda rule: rule.endpoint.startswith(
            #     'should_be_v1_only'
            # ),
            # # definition_filter is optional
            # # it is a callable to filter the definition models to include
            # "definition_filter": lambda definition: (
            #     'v1_model' in definition.tags)
        },
        {
            "version": "0.0.2",
            "title": "Api v2",
            "description": 'This is the version 2 of our API',
            "endpoint": 'v2_spec',
            "route": '/v2/spec',
            # "rule_filter": lambda rule: rule.endpoint.startswith(
            #     'should_be_v2_only'
            # ),
            # "definition_filter": lambda definition: (
            #     'v2_model' in definition.tags)
        }
    ]
}
