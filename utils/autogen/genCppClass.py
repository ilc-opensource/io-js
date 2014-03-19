def GenClass(module, name, c):
  s = \
'''
#include <node.h>

class %sV8:: public node::ObjectWrap {

public:
    static void Init(v8::Handle<v8::Object> exports);

private:
    %s *m_val;
    ~%sV8();
    static v8::Handle<v8::Value> New(const v8::Arguments& args);
    static v8::Persistent<v8::Function> constructor;
'''%(name, name, name)

  for m in c["methods"]["public"]:
    s += \
'''
    static v8::Handle<v8::Value> %sconst v8::Arguments& args);''' \
    % m["name"]

  s += "\n};\n"
