#include <iostream>
#include <capnp/message.h>
#include <capnp/serialize.h>

#include "enum.capnp.h"


std::ostream& operator<<(std::ostream& out, const Temperature::Unit unit){
    switch(unit){
    case (Temperature::Unit::K):
        return out << "K";
    case (Temperature::Unit::F):
        return out << "F";
    case (Temperature::Unit::C):
        return out << "C";
    }
}

int main(void) {
    capnp::MallocMessageBuilder message;
    Temperature::Builder temperature = message.initRoot<Temperature>();

    temperature.setValue(100.0);
    temperature.setUnit(Temperature::Unit::C);

    std::cout << "(value = " << temperature.getValue() << ", unit = " << temperature.getUnit() << ")" << std::endl;
    // auto bytes = capnp::messageToFlatArray(message).asBytes();
    // auto words = capnp::messageToFlatArray(message);

    return 0;
}
