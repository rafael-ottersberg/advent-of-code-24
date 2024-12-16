add_library( day16 day16.cpp)

target_include_directories(day16 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day16 TBB::tbb )