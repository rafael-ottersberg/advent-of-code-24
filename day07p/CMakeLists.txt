add_library( day07p day07.cpp)

target_include_directories(day07p PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day07p TBB::tbb )