add_library( day08 day08.cpp)

target_include_directories(day08 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day08 TBB::tbb )